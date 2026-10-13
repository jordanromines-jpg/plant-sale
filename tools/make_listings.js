// Builds LISTINGS.md from plants.js. Run: node tools/make_listings.js
const path = require("path");
const fs = require("fs");
global.window = {};
require(path.join(__dirname, "..", "plants.js"));
const { SALE, PLANTS } = window.PLANT_SALE;
const HEALTH = "Healthy and disease-free. It lives in a humid room and is putting out new growth.";

let out = "# Listings\n\nPaste these into Facebook Marketplace, Craigslist or OfferUp. Each block gives the title, the price and the description. Lead with the title as written: it starts with the name buyers search for. The link in each description opens that plant on the sale page.\n\nAfter editing `plants.js`, rebuild this file with `node tools/make_listings.js`.\n";
for (const p of PLANTS) {
  const price = `$${p.price}${p.unit ? " " + p.unit : ""}`;
  const details = [
    ["Plant", p.name], ["Scientific name", p.sci], ["Available", p.count], ["Size", p.size], ["Pot", p.pot],
    ["Comes with", p.includes], ["Light", p.light], ["Water", p.water], ["Pets", p.pets],
  ].filter(r => r[1]).map(([k, v]) => `${k}: ${v}`);
  const lines = [p.pitch, "", ...details, "", HEALTH, `Pickup in ${SALE.pickup}.`, "",
    "More photos of this plant, and everything else I have for sale:", `${SALE.url}#p${p.n}`, "", "If it's listed, it's still available."];
  out += `\n## ${String(p.n).padStart(2, "0")}. ${p.name}\n\nTitle: ${p.title}\nPrice: ${price}\n\n\`\`\`text\n${lines.join("\n")}\n\`\`\`\n`;
}
fs.writeFileSync(path.join(__dirname, "..", "LISTINGS.md"), out);
console.log(`Wrote ${PLANTS.length} listings`);
