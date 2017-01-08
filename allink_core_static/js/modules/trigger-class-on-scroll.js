export function triggerClassOnScroll(options) {
    if (!options.element) {
        console.error('triggerClassOnScroll: No element set');
    }

    let class_to_trigger = options.class_to_trigger,
        scroll = options.scroll || 0,
        element = options.element;

    const scrollHandler = function () {
        if(window.scrollY >= scroll && !element.classList.contains(class_to_trigger)) {
            element.classList.add(class_to_trigger);
        }
        else if(window.scrollY < scroll && element.classList.contains(class_to_trigger)) {
            element.classList.remove(class_to_trigger);
        }
    };

    window.addEventListener('scroll', () => {
        scrollHandler();
    });

    scrollHandler();

    return this;
}
