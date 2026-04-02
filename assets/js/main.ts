import { openActiveNavTree, enableNavAccordionLinks, fixAccordionRoles } from './nav'
import { resizePageHeight } from './page'

openActiveNavTree()
enableNavAccordionLinks()
resizePageHeight()

// UIkit adds role="region" to <ul> accordion elements which is invalid per ARIA specs.
// Wait for UIkit to initialize, then remove the invalid roles.
window.addEventListener('load', fixAccordionRoles)

