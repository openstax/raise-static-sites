export const resizePageHeight = (): void => {
    const footer = document.querySelector<HTMLElement>('footer')
    const pageClassElement = document.querySelector<HTMLElement>('.page')
    let previousFooterHeight = footer.clientHeight
    pageClassElement.style.height = `calc(100vh - var(--header-height) - ${previousFooterHeight}px)`

    const resizeObserver = new ResizeObserver((entries) => {
        for (const entry of entries) {
            if (previousFooterHeight !== entry.borderBoxSize[0].blockSize) {
                pageClassElement.style.height = `calc(100vh - var(--header-height) - ${entry.borderBoxSize[0].blockSize}px)`
                previousFooterHeight = entry.borderBoxSize[0].blockSize
            }
        }
    })
    
    resizeObserver.observe(footer)
}