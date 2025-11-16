import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// Create a Head instance and attach site-wide custom CSS via the component's
// `css` property. This gets picked up by the component resource collector and
// bundled into the generated `index.css` so the styles are available on every
// page without editing the Head component itself.
const HeadWithCustomCSS = Component.Head()
HeadWithCustomCSS.css = `
/* ---- Site custom CSS (edit in quartz.layout.ts) ---- */
.callout[data-callout="proof"] {--callout-color: 54,152,142; --callout-icon: notebook-pen;}
img[alt*="centre"] {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
img[alt*="float-left"] {
    display: block;
    float:left;
    margin-left:0.5em;
    margin-right:0.5em;
}
img[alt*="float-right"] {
    display:block;
    float:right;
    margin-left: 0.5em;
    margin-right: 0.5em;
}
.cm-line:has(+ .cm-embed-block.cm-table-widget) br {
  display: none;
}

/* --------------------------------------------------- */
`

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: HeadWithCustomCSS,
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
