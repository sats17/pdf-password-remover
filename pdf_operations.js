const { PDFDocument } = PDFLib;
 
 console.log("From script")

 function renderPdf(uint8array) {
    const tempblob = new Blob([uint8array], {
      type: "application/pdf",
    });
    const docUrl = URL.createObjectURL(tempblob);
    setPdfFileData(docUrl);
  }

  function range(start, end) {
    let length = end - start + 1;
    return Array.from({ length }, (_, i) => start + i - 1);
  }

  async function extractPdfPage(arrayBuff) {
    const pdfSrcDoc = await PDFDocument.load(arrayBuff, { ignoreEncryption: true});
    const pdfNewDoc = await PDFDocument.create();
    const pages = await pdfNewDoc.copyPages(pdfSrcDoc, range(2, 3));
    pages.forEach((page) => pdfNewDoc.addPage(page));
    const newpdf = await pdfNewDoc.save();
    return newpdf;
  }

 function readFileAsync(file) {
    return new Promise((resolve, reject) => {
      let reader = new FileReader();
      reader.onload = () => {
        console.log("On load reader clicked")
        resolve(reader.result);
      };
      reader.onerror = reject;
      reader.readAsArrayBuffer(file);
      console.log("After read as array")
    });
  }

  const onFileSelected = async (e) => {
    console.log("On file selected")
    const fileList = e.target.files;
    console.log(fileList)
    var filename = fileList[0].name;
    console.log(filename)
    if (fileList?.length > 0) {
       console.log("Read file")
      const pdfArrayBuffer = await readFileAsync(fileList[0]);
      console.log(pdfArrayBuffer)
      const newPdfDoc = await extractPdfPage(pdfArrayBuffer);
      renderPdf(newPdfDoc);
    }
    
 };


 const fileSelector = document.querySelector('input#fileSelector');
 fileSelector.addEventListener('change', onFileSelected, false);
 var filename = fileSelector.files;
 console.log(filename)

