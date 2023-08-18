
template = """<tbody>
                <tr>
                    <td align=\"center\"> 
                      <audio id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples/GT/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples/wavegrad/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples/diffwave/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples/priorgrad/{filename}\"></audio>
                    </td>
                    <td align=\"center\"> 
                      <audio  id=\"player\" controls=\"\"><source src=\"static/FREGRAD_mos_samples/fregrad/{filename}\"></audio>
                    </td>
                </tr>
              </tbody>"""

filelist = [f.strip() for f in open("samples.txt")][:10]
for f in filelist:
    print(template.format(filename=f))