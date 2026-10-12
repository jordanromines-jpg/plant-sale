// Builds LISTINGS.md from plants.js. Run: node tools/make_listings.js
const path = require("path");
const fs = require("fs");
global.window = {};
require(path.join(__dirname, "..", "plants.js"));
const { SALE, PLANTS } = window.PLANT_SALE;
const HEALTH = "Healthy and disease-free. It lives in a humid room and is putting out new growth.";

let out = "# Listings\n\nPaste these into Facebook Marketplace, Craigslist or OfferUp. Each block gives the title, the price and the description. The link in each description opens that plant on the sale page.\n\nAfter editing `plants.js`, rebuild this file with `node tools/make_listings.js`.\n";
for (const p of PLANTS) {
  const lines = [p.pitch, "", p.care, "", HEALTH];
  if (p.includes) lines.push(`Comes with the ${p.includes.toLowerCase()}.`);
  lines.push(`Pickup in ${SALE.pickup}.`, "", "More photos of this plant, and everything else I have for sale:", `${SALE.url}#p${p.n}`, "", "If it's listed, it's still available.");
  const price = `$${p.price}${p.unit ? " " + p.unit : ""}`;
  out += `\n## ${String(p.n).padStart(2, "0")}. ${p.name}\n\nTitle: ${p.title}\nPrice: ${price}\n\n\`\`\`text\n${lines.join("\n")}\n\`\`\`\n`;
}
fs.writeFileSync(path.join(__dirname, "..", "LISTINGS.md"), out);
console.log(`Wrote ${PLANTS.length} listings`);
