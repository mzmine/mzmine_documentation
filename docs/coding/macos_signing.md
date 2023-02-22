# macOS code signing

Code signing is a security feature provided by Apple's macOS that allows developers to digitally sign their applications and verify their identity. This ensures that the application is not tampered with or altered by a third party, and that it can be trusted by users.

MZmine 3 codebase is signed with the Developer ID Application Certificate of the Czech Technical University in Prague (`"Developer ID Application: Ceske vysoke uceni technicke v Praze (LK4H72N842)"`) under the Apple ID `mzmine.devel@gmail.com`. The procedure is implemented in the [gradle build file](https://github.com/mzmine/mzmine3/blob/master/build.gradle) and consists of three main steps described below: signing, notarization, and stapling.

## Signing

Signing is a step embedding a digital signature in the MZmine codebase, which allows macOS to verify the integrity of the application before it is run.

The necessary condition for the code signing is a Developer ID Application certificate from a Certificate Authority, which is the Czech Technical University in Prague in our case. `base64`-encoded certificated and the associated password are stored as GitHub secrets under the names `MACOS_DEVELOPER_CERTIFICATE` and `MACOS_DEVELOPER_CERTIFICATE_PWD` respectively. In order to use the certificate in [CI/CD build of MZmine](https://github.com/mzmine/mzmine3/blob/e35aceb5a0737a184038b4749b7e29646172954d/.github/workflows/dev_build_release.yml#L96), we add it to macOS keychain with `security set-key-partition-list` command following [Jan Bílek's tutorial](https://localazy.com/blog/how-to-automatically-sign-macos-apps-using-github-actions).

!!! info
    Notice, that the Developer ID Application certificate is not publicly available. Therefore, a manually built version of MZmine cannot be signed. Nevertheless, it still can be normally built.

To sign MZmine code with the certificate, `jpackage` utility needs to be supplied with an additional (constant) argument `--mac-sign` and its dependencies such as `--mac-package-identifier "io.github.mzmine.main"` and `--mac-signing-key-user-name "Developer ID Application: Ceske vysoke uceni technicke v Praze (LK4H72N842)"`. Nevertheless, `jpackage` is not able to automatically sign all native libraries. For that reason, we manually traverse the entire codebase and sign all such libraries which can be classified into three categories:
1. Any file with one of the following extensions: `.dylib`, `.so`, `.dll`, `.a`, `.lib`.
2. Any file with an extension from point 1. but nested inside of `.jar` archives.
3. Content of ThermoRawFileParser `.zip` archive.

The libraries are signed with

```shell
codesign --deep --force --timestamp -s ${developerID} --options runtime --entitlements ${entitlementsPth} -f -v ${p}
```
, where `${deveperID}` is `"Developer ID Application: Ceske vysoke uceni technicke v Praze (LK4H72N842)"`, `${entitlementsPth}` contains [privileges](https://github.com/mzmine/mzmine3/blob/master/gradle/macos.entitlements) granted to the MZmine executable, and `${p}` is a path to the file to be signed. The files nested in archives are unarchived, signed, and then archived back.

## Notarization

Notarization is an additional security step that is performed by Apple after an application is signed and is required to distribute MZmine outside of the Mac App Store. During this step signed MZmine code is uploaded to Apple's servers, where it is scanned for malware and other malicious content. Note, that this procedure usually takes around 10 minutes to be completed.

The notarization is performed using `xcrun notarytool` utility

```shell
xcrun notarytool submit --wait --apple-id ${appleID} --password ${appleIDPassword} --team-id ${appleTeamID} "MZmine_macOS_portable.zip"
```

, where `${appleTeamID}` is `mzmine.devel@gmail.com` and `${appleTeamID}` is the team of the Developer ID - `LK4H72N842`.

## Stapling

Stapling is the process of attaching a notarization ticket to a signed application. When an application is stapled, the notarization ticket is embedded in the application's code, which allows macOS to verify the notarization status of the application even if it is not connected to the internet.

Stapling is performed with

```shell
xcrun stapler staple "MZmine.app"
```

## Distribution of disk image
The output of the steps described above is signed portable MZmine `.app`. Since it is more convenient to distribute macOS software as a `.dmg` disk image, we additionally pack the portable into `.dmg` using [`appdmg`](https://github.com/LinusU/node-appdmg) utility.
