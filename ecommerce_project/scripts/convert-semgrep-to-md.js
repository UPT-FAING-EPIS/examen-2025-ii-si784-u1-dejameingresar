// Simple converter: semgrep JSON -> markdown summary
const fs = require('fs');
const inFile = process.argv[2] || 'reports/semgrep-report.json';
const outFile = process.argv[3] || 'reports/semgrep-report.md';
if (!fs.existsSync(inFile)) {
  console.error('Input not found', inFile);
  process.exit(1);
}
const data = JSON.parse(fs.readFileSync(inFile, 'utf8'));
let md = '# Semgrep Report\n\n';
if (!data.results || data.results.length===0) {
  md += 'No issues found.\n';
} else {
  for (const r of data.results) {
    md += `## ${r.check_id} - ${r.extra.message}\n`;
    md += `- Path: ${r.path}\n`;
    md += `- Severity: ${r.extra.severity}\n\n`;
  }
}
fs.mkdirSync(require('path').dirname(outFile), {recursive:true});
fs.writeFileSync(outFile, md);
console.log('Wrote', outFile);
