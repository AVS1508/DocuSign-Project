import wkhtmltopdf from "wkhtmltopdf";

function convert() {
  console.log("Conversion in Progress...");
  wkhtmltopdf("http://google.com/", { pageSize: "letter" }).pipe(
    fs.createWriteStream("out.pdf")
  );
}
