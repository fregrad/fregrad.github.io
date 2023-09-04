
template = """
              <tbody>
                <tr>
                    <td align=\"center\"> 
                      <audio id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/GT/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/wavegrad/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/diffwave/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/priorgrad/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/fregrad/{filename}\"></audio>
                    </td>
                </tr>
              </tbody>"""
import os
filelist = os.listdir('static/FREGRAD_mos_samples_fast/diffwave')
for f in filelist:
    print(template.format(filename=f))


template = """
              <tbody>
                <tr>
                    <td align=\"center\"> 
                      <audio id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/GT/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/wavegrad/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/diffwave/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/priorgrad/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples_fast/fregrad/{filename}\"></audio>
                    </td>
                </tr>
              </tbody>"""
import os
filelist = os.listdir('static/FREGRAD_mos_samples_fast/diffwave')
for f in filelist:
    print(template.format(filename=f))