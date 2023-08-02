window.onload = function () {
  document.getElementById("download").addEventListener("click", () => {
    const pdf = this.document.getElementById("pdf");
    let pdName = document.getElementById("pdfName");
    let name = pdName.innerHTML.slice(6);
    var opt = {
      margin: [0.2, 0.3, 0.2, 0.2],
      filename: name + "onliineTaxComputation.pdf",
      image: { type: "png", quality: 1 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: "in", format: "a4", orientation: "portrait" },
    };
    html2pdf().from(pdf).set(opt).save();
  });
};
