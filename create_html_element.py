
# template = """
#               <tbody>
#                 <tr>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples/GT/{img_filename}" width="300" alt>
#                       <br>
#                       <audio id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/GT/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\"> 
#                       <br>
#                       <img src="static/FREGRAD_mos_samples/wavegrad/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/wavegrad/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples/diffwave/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/diffwave/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\"> 
#                       <br>
#                       <img src="static/FREGRAD_mos_samples/priorgrad/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/priorgrad/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples/fregrad/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/fregrad/{filename}\"></audio>
#                     </td>
#                 </tr>
#               </tbody>"""
# # import os
# # filelist = [f for f in os.listdir('static/FREGRAD_mos_samples/diffwave') if '.wav' in f]
# # for f in filelist:
# #     print(template.format(filename=f, img_filename=f.replace('.wav', '.png')))


# template = """
#               <tbody>
#                 <tr>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples_fast/GT/{img_filename}" width="300" alt>
#                       <br>
#                       <audio id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/GT/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples_fast/wavegrad/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/wavegrad/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples_fast/diffwave/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/diffwave/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples_fast/priorgrad/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/priorgrad/{filename}\"></audio>
#                     </td>
#                     <td align=\"center\">
#                       <br>
#                       <img src="static/FREGRAD_mos_samples_fast/fregrad/{img_filename}" width="300" alt>
#                       <br>
#                       <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/fregrad/{filename}\"></audio>
#                     </td>
#                 </tr>
#               </tbody>"""
# import os
# filelist = [f for f in os.listdir('static/FREGRAD_mos_samples_fast/diffwave') if '.wav' in f]
# for f in filelist:
#     print(template.format(filename=f, img_filename=f.replace('.wav', '.png')))

template = """
              <tbody>
                <tr>
                    <td align=\"center\">
                      <br>
                      <img src="static/FREGRAD_cmos_samples/our/{img_filename}" width="150" alt>
                      <br>
                      <audio id=\"player\" controls=\"\"><source src=\"static/FREGRAD_cmos_samples/our/{filename}\"></audio>
                    </td>
                    <td align=\"center\">
                      <br>
                      <img src="static/FREGRAD_mos_samples_FREGRAD_cmos_samplesfast/no_freq_block/{img_filename}" width="150" alt>
                      <br>
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_cmos_samples/no_freq_block/{filename}\"></audio>
                    </td>
                    <td align=\"center\">
                      <br>
                      <img src="static/FREGRAD_cmos_samples/no_sep_prior/{img_filename}" width="150" alt>
                      <br>
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_cmos_samples/no_sep_prior/{filename}\"></audio>
                    </td>
                    <td align=\"center\">
                      <br>
                      <img src="static/FREGRAD_cmos_samples/no_zero_snr/{img_filename}" width="150" alt>
                      <br>
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_cmos_samples/no_zero_snr/{filename}\"></audio>
                    </td>
                </tr>
              </tbody>"""
import os
filelist = [f for f in os.listdir('static/FREGRAD_cmos_samples/our') if '.wav' in f][:5]
for f in filelist:
    print(template.format(filename=f, img_filename=f.replace('.wav', '.png')))