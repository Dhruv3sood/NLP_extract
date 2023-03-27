k=0
for i in data:
  k=k+1
print(k)

def main_function(filename):
    #image_dir = document_in_path + filename
    pages = convert_from_path(filename)
    i=1
    for page in pages:
        # page.save('Invoice Bill Scanned.jpg', 'JPEG')
        image_name = "Page_" + str(i) + ".jpg"
https://colab.research.google.com/drive/1GeBzgBLtuFTYhcPAcj_uBbKLWKaeoHrH#scrollTo=KaCsENqRkLhV&printMode=true 2/3
        page.save(image_name, 'JPEG')
        i+=1
if __name__=="__main__":
    filename = "/content/COMPLAINT  No  91 OF  2016.pdf"
    main_function(filename)
    
    
