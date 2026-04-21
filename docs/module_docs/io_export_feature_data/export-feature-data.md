# Export feature data

This module will export the data of all features in a feature list to a file.

:material-menu-open: **Feature list methods → Export feature list → Export feature data**

## Parameters

#### Feature lists

Select the feature list(s) you want to export to a file. If multiple feature lists shall be
exported, make sure to use the placeholder `{}` in the [Export file name](#export-file-name).

#### Export file name

Specify the name of the file to export the feature data into. Use `{}` to automatically insert the
name of the respective exported feature list.

#### Export format

Specify the export format. XML is currently the only available option.

An example XML file may look like this (Some entries were removed to keep it more or less concise):

```XML
<?xml version='1.0' encoding='UTF-8'?>
<featurelist
  featurelistname="Aligned feature list 13C peak gaps dup corr PEARSON r greq 0.85 dp greq 5"
  numberofrows="4204" date="2025/05/16 12:15:41">
  <row id="49">
    <datatype type="area">3262872.0</datatype>
    <datatype type="rt">0.32390267</datatype>
    <datatype type="mz_range">[175.11827087402344;175.1194610595703]</datatype>
    <datatype type="charge">1</datatype>
    <datatype type="fragment_scans">
      <scan scantype="simplescan" rawdatafile="171103_PMA_TK_media_02.mzML" scanindex="151"/>
      <scan scantype="simplescan" rawdatafile="171103_PMA_TK_media_03.mzML" scanindex="153"/>
    </datatype>
    <datatype type="feature_shape">true</datatype>
    <datatype type="alignment_scores">
      <subtypes>
        <datatype type="rate">0.3043478</datatype>
        <datatype type="aligned_features_n">7</datatype>
        <datatype type="align_extra_features">5</datatype>
        <datatype type="weighted_distance_score">0.8496631</datatype>
        <datatype type="mz_diff_ppm">4.4820127</datatype>
        <datatype type="mz_diff">7.84884589847934E-4</datatype>
        <datatype type="rt_absolute_error">0.021971852</datatype>
        <datatype type="ion_mobility_absolute_error">0.0</datatype>
      </subtypes>
    </datatype>
    <datatype type="rt_range">[0.30016744;0.44724196]</datatype>
    <datatype type="mz">175.11891174473593</datatype>
    <datatype type="spectral_db_matches">
      <feature_annotation annotation_type="spectral_library_annotation">
        <spectraldatabaseentry library_file="MoNA-export-LC-MS-MS_Spectra.json (150211 spectra)">
          <mzs>
            60.05536;70.06634;72.08131;112.0877;114.1043;115.0878;116.0718;130.0988;157.1094;158.0937;175.1232
          </mzs>
          <intensities>
            50.218311;69.503389;4.296692;4.05231;1.387287;1.208214;38.124055;16.18238;2.837249;14.222061;100.0
          </intensities>
          <databasefieldslist>
            <entry name="INSTRUMENT_TYPE">LC-ESI-QTOF</entry>
            <entry name="MS_LEVEL">MS2</entry>
            <entry name="INCHI">
              InChI=1S/C6H14N4O2/c7-4(5(11)12)2-1-3-10-6(8)9/h4H,1-3,7H2,(H,11,12)(H4,8,9,10)/t4-/m0/s1
            </entry>
            <entry name="PRECURSOR_MZ">175.118957519531</entry>
            <entry name="POLARITY">positive</entry>
            <entry name="ION_TYPE">[M+H]+</entry>
            <entry name="ION_SOURCE">ESI</entry>
            <entry name="DATA_COLLECTOR">Isabel Meister, Romanas Chaleckis</entry>
            <entry name="SMILES">O=C(O)C(N)CCCNC(=N)N</entry>
            <entry name="PRINCIPAL_INVESTIGATOR">Isabel Meister, Romanas Chaleckis</entry>
            <entry name="INCHIKEY">ODKSFYDXXFIFQN-BYPYZUCNSA-N</entry>
            <entry name="FORMULA">C6H14N4O2</entry>
            <entry name="NAME">Arginine; LC-tDDA; CE10</entry>
            <entry name="RT">12.65</entry>
            <entry name="INSTRUMENT">Agilent 6550 iFunnel</entry>
            <entry name="COLLISION_ENERGY">10</entry>
          </databasefieldslist>
        </spectraldatabaseentry>
        <spectralsimilarity>
          <similairtyfunction>Weighted cosine similarity</similairtyfunction>
          <overlappingpeaks>10</overlappingpeaks>
          <score>0.991997389209482</score>
          <explainedLibraryIntensity>1.0</explainedLibraryIntensity>
          <libraryspectrum>
            <mzs>
              60.05536;70.06634;72.08131;112.0877;114.1043;115.0878;116.0718;130.0988;157.1094;158.0937
            </mzs>
            <intensities>
              50.218311;69.503389;4.296692;4.05231;1.387287;1.208214;38.124055;16.18238;2.837249;14.222061
            </intensities>
          </libraryspectrum>
          <queryspectrum>
            <mzs>
              60.05648689221877;70.06589447026973;72.08146690621223;112.08713629620883;114.10296712134367;115.0865468821093;116.0707957060524;130.09748713358292;157.10848530129516;158.09225213474215
            </mzs>
            <intensities>
              1.700311924990654E7;2.792031528575635E7;5692692.274521589;2063768.8710607588;505617.66608789563;535806.9913217761;1.6561022981089354E7;6705487.050384879;1057548.0377922803;5742073.7107543945
            </intensities>
          </queryspectrum>
          <alignedspectrumlist numvalues="2">
            <alignedspectrum>
              <mzs>
                60.05536;70.06634;72.08131;112.0877;114.1043;115.0878;116.0718;130.0988;157.1094;158.0937
              </mzs>
              <intensities>
                50.218311;69.503389;4.296692;4.05231;1.387287;1.208214;38.124055;16.18238;2.837249;14.222061
              </intensities>
            </alignedspectrum>
            <alignedspectrum>
              <mzs>
                60.05648689221877;70.06589447026973;72.08146690621223;112.08713629620883;114.10296712134367;115.0865468821093;116.0707957060524;130.09748713358292;157.10848530129516;158.09225213474215
              </mzs>
              <intensities>
                1.700311924990654E7;2.792031528575635E7;5692692.274521589;2063768.8710607588;505617.66608789563;535806.9913217761;1.6561022981089354E7;6705487.050384879;1057548.0377922803;5742073.7107543945
              </intensities>
            </alignedspectrum>
          </alignedspectrumlist>
        </spectralsimilarity>
        <ccserror>NULL_VALUE</ccserror>
        <testedmz>175.11891174473593</testedmz>
        <testedrt>0.32390267</testedrt>
        <scan scantype="simplemergedmsmsspectrum" mslevel="2" merge_spec_type="SAME_ENERGY"
          ce="30.0" mergingtype="MAXIMUM" rawdatafile="171103_PMA_TK_media_05.mzML">
          <msmsinfo type="ddamsmsinfo" precursormz="175.118453979492" charge="1" energy="30.0"
            activationtype="HCD" mslevel="2" isolationwindow="[174.618453979492;175.618453979492]"/>
          <mzs>
            60.05648689221877;70.06589447026973;72.08146690621223;112.08713629620883;114.10296712134367;115.0865468821093;116.0707957060524;130.09748713358292;157.10848530129516;158.09225213474215;175.118826887203
          </mzs>
          <intensities>
            1.700311924990654E7;2.792031528575635E7;5692692.274521589;2063768.8710607588;505617.66608789563;535806.9913217761;1.6561022981089354E7;6705487.050384879;1057548.0377922803;5742073.7107543945;2.654460362855494E7
          </intensities>
          <scans rawdatafile="171103_PMA_TK_media_03.mzML">{153}[]</scans>
          <scans rawdatafile="171103_PMA_TK_media_06.mzML">{149}[]</scans>
          <scans rawdatafile="171103_PMA_TK_media_04.mzML">{144}[]</scans>
          <scans rawdatafile="171103_PMA_TK_media_05.mzML">{150}[]</scans>
          <scans rawdatafile="171103_PMA_TK_media_02.mzML">{151}[]</scans>
        </scan>
      </feature_annotation>
    </datatype>
    <datatype type="intensity_range">[171891.52;7.5953896E7]</datatype>
    <datatype type="feature_group">27</datatype>
    <datatype type="id">49</datatype>
    <datatype type="height">7.5953896E7</datatype>
    <feature rawdatafile="171103_PMA_TK_M1_01.mzML">
      <datatype type="area">28286.621</datatype>
      <datatype type="rt">0.32012287</datatype>
      <datatype type="mz_range">[175.11862182617188;175.11878967285156]</datatype>
      <datatype type="best_ms1_scan_number">
        <scan scantype="simplescan" rawdatafile="171103_PMA_TK_M1_01.mzML" scanindex="144"/>
      </datatype>
      <datatype type="fwhm">0.019634774</datatype>
      <datatype type="rt_range">[0.30645204;0.34960598]</datatype>
      <datatype type="feature_state">ESTIMATED</datatype>
      <datatype type="datafile">171103_PMA_TK_M1_01.mzML</datatype>
      <datatype type="mz">175.11867991636373</datatype>
      <datatype type="intensity_range">[290797.88;1358260.6]</datatype>
      <datatype type="asymmetry_factor">2.1566434</datatype>
      <datatype type="feature_data">
        <feature_data>
          <simpleiontimeseries>
            <scans numvalues="7">136;140;144;148;152;156;160</scans>
            <intensities numvalues="7">
              0.0;584109.4375;1358260.625;1170476.875;665673.75;290797.875;0.0
            </intensities>
            <mzs numvalues="7">
              175.11877432337528;175.1186981201172;175.11862182617188;175.11865234375;175.11878967285156;175.1187744140625;175.11877432337528
            </mzs>
            <rts numvalues="7">
              0.30645203590393066;0.3132686913013458;0.3201228678226471;0.32709363102912903;0.3339269161224365;0.3407540023326874;0.3496059775352478
            </rts>
          </simpleiontimeseries>
        </feature_data>
      </datatype>
      <datatype type="tailing_factor">1.5783217</datatype>
      <datatype type="height">1358260.6</datatype>
    </feature>
    <feature rawdatafile="171103_PMA_TK_M1_02.mzML">
      <datatype type="area">26188.146</datatype>
      <datatype type="rt">0.31954175</datatype>
      <datatype type="mz_range">[175.11877432337528;175.1194610595703]</datatype>
      <datatype type="best_ms1_scan_number">
        <scan scantype="simplescan" rawdatafile="171103_PMA_TK_M1_02.mzML" scanindex="144"/>
      </datatype>
      <datatype type="fwhm">0.02036497</datatype>
      <datatype type="rt_range">[0.30587724;0.34912074]</datatype>
      <datatype type="feature_state">ESTIMATED</datatype>
      <datatype type="datafile">171103_PMA_TK_M1_02.mzML</datatype>
      <datatype type="mz">175.11930236793012</datatype>
      <datatype type="intensity_range">[222693.89;1360981.8]</datatype>
      <datatype type="asymmetry_factor">1.7352959</datatype>
      <datatype type="feature_data">
        <feature_data>
          <simpleiontimeseries>
            <scans numvalues="7">136;140;144;148;152;156;160</scans>
            <intensities numvalues="7">
              0.0;881861.4375;1360981.75;924455.9375;405910.3125;222693.890625;0.0
            </intensities>
            <mzs numvalues="7">
              175.11877432337528;175.1192169189453;175.11924743652344;175.1194305419922;175.11929321289062;175.1194610595703;175.11877432337528
            </mzs>
            <rts numvalues="7">
              0.3058772385120392;0.3126917779445648;0.3195417523384094;0.3263646066188812;0.33320000767707825;0.34002700448036194;0.34912073612213135
            </rts>
          </simpleiontimeseries>
        </feature_data>
      </datatype>
      <datatype type="tailing_factor">1.5823284</datatype>
      <datatype type="height">1360981.8</datatype>
    </feature>
    <feature rawdatafile="171103_PMA_TK_M1_03.mzML">
      <datatype type="area">19992.443</datatype>
      <datatype type="rt">0.32646403</datatype>
      <datatype type="mz_range">[175.11877432337528;175.1190643310547]</datatype>
      <datatype type="best_ms1_scan_number">
        <scan scantype="simplescan" rawdatafile="171103_PMA_TK_M1_03.mzML" scanindex="148"/>
      </datatype>
      <datatype type="fwhm">0.021426953</datatype>
      <datatype type="rt_range">[0.30597037;0.34899095]</datatype>
      <datatype type="feature_state">ESTIMATED</datatype>
      <datatype type="datafile">171103_PMA_TK_M1_03.mzML</datatype>
      <datatype type="mz">175.1189857310156</datatype>
      <datatype type="intensity_range">[269273.7;865271.25]</datatype>
      <datatype type="asymmetry_factor">1.0992143</datatype>
      <datatype type="feature_data">
        <feature_data>
          <simpleiontimeseries>
            <scans numvalues="7">136;140;144;148;152;156;160</scans>
            <intensities numvalues="7">
              0.0;367347.625;859838.75;865271.25;523678.3125;269273.6875;0.0
            </intensities>
            <mzs numvalues="7">
              175.11877432337528;175.11904907226562;175.11891174316406;175.11898803710938;175.1190185546875;175.1190643310547;175.11877432337528
            </mzs>
            <rts numvalues="7">
              0.30597037076950073;0.31278908252716064;0.31963691115379333;0.3264640271663666;0.33330148458480835;0.34013262391090393;0.34899094700813293
            </rts>
          </simpleiontimeseries>
        </feature_data>
      </datatype>
      <datatype type="tailing_factor">1.0496072</datatype>
      <datatype type="height">865271.25</datatype>
    </feature>
  </row>
</featurelist>
```
