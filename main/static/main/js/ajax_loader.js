// code has been stolen from https://www.youtube.com/watch?v=DVVPK-xrGV4 (successful)

document.addEventListener("DOMContentLoaded", () => {
    var oldContent = document.getElementById('mainCommentsContainer').innerHTML;

    const loadPage = () => {
        var currentUrl = window.location.href;

        fetch(currentUrl)
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');

                const newContent = doc.getElementById('mainCommentsContainer').innerHTML;

                if (newContent != oldContent) {
                    document.getElementById('mainCommentsContainer').innerHTML = newContent;
                    oldContent = newContent;
                }
            });
    };

    setInterval(loadPage, 1 * 1000);
});