export const enableNavAccordionLinks = (): void => {
  const navLinks = document.querySelectorAll<HTMLAnchorElement>('nav a.uk-accordion-link')
  navLinks.forEach((elem) => {
    elem.onclick = (event) => { event.stopPropagation() }
  })
}

export const openActiveNavTree = (): void => {
  const openNavLink = document.querySelector<HTMLElement>('nav .active')

  if (openNavLink === null) {
    return
  }

  let currentListElement: HTMLElement | null = openNavLink

  while (currentListElement !== null) {
    if (currentListElement.tagName === 'LI') {
      currentListElement.classList.add('uk-open')
    }
    currentListElement = currentListElement.parentElement
  }
}
