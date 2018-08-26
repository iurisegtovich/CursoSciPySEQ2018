for file in *.odp
do
  libreoffice --headless --convert-to pdf --outputfile ../arquivos_pdf/$(file).pdf file
done
