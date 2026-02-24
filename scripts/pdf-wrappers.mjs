import fs from "fs"
import path from "path"

const contentDir = "./content"

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name)

    if (entry.isDirectory()) {
      walk(fullPath)
      continue
    }

    if (!entry.name.endsWith(".pdf")) continue

    const baseName = entry.name.replace(".pdf", "")
    const mdPath = path.join(dir, `${baseName}.md`)
    const pdfRelative = `./${entry.name}`

    const wrapperContent = `---
title: ${baseName}
type: pdf
tags:
  - pdf
---

[Open PDF](${pdfRelative})

<iframe src="${pdfRelative}" width="100%" height="800px"></iframe>
`

    if (!fs.existsSync(mdPath)) {
      fs.writeFileSync(mdPath, wrapperContent)
      console.log(`✓ Created wrapper: ${mdPath}`)
    }
  }
}

function cleanStaleWrappers(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name)

    if (entry.isDirectory()) {
      cleanStaleWrappers(fullPath)
      continue
    }

    if (!entry.name.endsWith(".md")) continue

    const mdContent = fs.readFileSync(fullPath, "utf8")
    if (!mdContent.includes("type: pdf")) continue

    const pdfPath = fullPath.replace(".md", ".pdf")

    if (!fs.existsSync(pdfPath)) {
      fs.unlinkSync(fullPath)
      console.log(`✗ Removed stale wrapper: ${fullPath}`)
    }
  }
}

cleanStaleWrappers(contentDir)
walk(contentDir)