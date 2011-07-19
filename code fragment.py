for i in range(len(t)):
     p = os.path.split(urlparse.urlsplit(t[i][1])[2])[0].split('/')[1:]
     if len(p) == 3 and p[2].isdigit():
         fd = open(p[1],'w')
         fd.write(t[i][3])
         fd.close()

