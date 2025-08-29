function convertMarkdown(mdText) {
  const regex = /!\[[^\]]*\]\((\/uploads\/[^\s)]+)\)/g;
  return mdText.replace(regex, (_, src) => `<img src='${src}' alt='' width='400'/>`);
}

const convertBtn = document.getElementById("convertBtn");
const copyBtn = document.getElementById("copyBtn");
const markdownArea = document.getElementById("markdown");
const outputArea = document.getElementById("output");

convertBtn.addEventListener("click", () => {
  const mdText = markdownArea.value;
  const converted = convertMarkdown(mdText);
  outputArea.textContent = converted;
});

copyBtn.addEventListener("click", () => {
  const converted = outputArea.textContent;
  navigator.clipboard.writeText(converted).then(() => {
    alert("✅ Copiado al portapapeles");
  });
});
