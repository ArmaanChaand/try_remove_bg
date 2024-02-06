(function () { const n = document.createElement("link").relList; if (n && n.supports && n.supports("modulepreload")) return; for (const e of document.querySelectorAll('link[rel="modulepreload"]')) o(e); new MutationObserver(e => { for (const t of e) if (t.type === "childList") for (const d of t.addedNodes) d.tagName === "LINK" && d.rel === "modulepreload" && o(d) }).observe(document, { childList: !0, subtree: !0 }); function r(e) { const t = {}; return e.integrity && (t.integrity = e.integrity), e.referrerPolicy && (t.referrerPolicy = e.referrerPolicy), e.crossOrigin === "use-credentials" ? t.credentials = "include" : e.crossOrigin === "anonymous" ? t.credentials = "omit" : t.credentials = "same-origin", t } function o(e) { if (e.ep) return; e.ep = !0; const t = r(e); fetch(e.href, t) } })(); const f = document.getElementById("menuBtn"), m = document.getElementById("sideNav"); try { f.addEventListener("click", function () { f.classList.toggle("OPEN"), document.body.classList.toggle("MENU_OPEN"), m.classList.toggle("OPEN") }), document.querySelectorAll("[data-faq-open-status]").forEach(a => { a.addEventListener("click", function () { this.dataset.faqOpenStatus == "open" ? this.dataset.faqOpenStatus = "close" : this.dataset.faqOpenStatus = "open" }) }); const n = document.getElementById("IMAGE_SLIDER"), r = n.parentElement; let o = !1, e = 0, t = 0; n.addEventListener("dragstart", function (a) { o = !0, e = a.clientX, a.dataTransfer.setDragImage(new Image, 0, 0), t = r.offsetWidth / r.parentElement.offsetWidth * 100 }), n.addEventListener("dragend", function (a) { o = !1 }), document.addEventListener("dragover", function (a) { if (a.preventDefault(), o) { const i = a.clientX - e; let c = t + i / r.parentElement.offsetWidth * 100; c = Math.max(Math.min(c, 100), 5), r.style.width = `${c}%` } }); const d = document.querySelectorAll("[data-image-input]"), l = document.getElementById("PREVIEW_SECTION"); d.forEach(a => { a.addEventListener("change", function () { var i = this.files[0], c = new FileReader; removeFetch(i); c.onload = function (u) { document.getElementById("UPLOADED_IMG").src = u.target.result, document.getElementById("PROCESSED_IMG").src = u.target.result, l.style.display = "flex", setTimeout(() => { console.log("LOADING") }, 2e3) }, c.readAsDataURL(i) }) }), document.getElementById("DOWNLOAD_IMG_BTN").addEventListener("click", function () { const a = document.getElementById("PROCESSED_IMG"); g(a) }) } catch (s) { console.log(s) } function g(s) { var n = document.createElement("canvas"); n.width = s.width, n.height = s.height; var r = n.getContext("2d"); r.drawImage(s, 0, 0); var o = n.toDataURL("image/webp"), e = document.createElement("a"); e.download = "WebP Background Remover.webp", e.href = o, e.click() }

const UPLOADED_IMG = document.getElementById('UPLOADED_IMG')
const PREVIEW_SECTION = document.getElementById('PREVIEW_SECTION')
const PROCESSED_IMG = document.getElementById('PROCESSED_IMG')
const dropArea = document.getElementById("IMAGE_FORM");
const errorMessage = document.getElementById("ERROR_MSG");


function removeFetch(file) {
    const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
    if (!file) {
        console.error('No file selected');
        return;
    }

    const formData = new FormData();
    formData.append('input_image', file);
    formData.append('csrfmiddlewaretoken', csrfmiddlewaretoken);
    PREVIEW_SECTION.classList.add('loading')
    dropArea.classList.remove('error')
    fetch('/remove/', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            console.log(response)
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const img_data = "data:image/webp;base64," + data.file_content;
            UPLOADED_IMG.src = img_data
            PROCESSED_IMG.src = img_data

        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            errorMessage.innerHTML = "It's not you. It's us. <br/> Sorry for the inconvenience."
            dropArea.classList.add('error')
            
        }).finally(() => {
            PREVIEW_SECTION.classList.remove('loading')
        })
}

const inputImage = document.getElementById("INPUT_IMAGE");

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false)
});

// Highlight drop area when item is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false)
});

['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false)
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
    e.preventDefault()
    e.stopPropagation()
}

function highlight() {
    dropArea.classList.add('dropped')
    dropArea.classList.remove('error')
}

function unhighlight() {
    dropArea.classList.remove('dropped')
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    
    // Take only the first file
    const file = files[0];

    if (file.type.startsWith('image/webp') && file.size < 10000000) {
    // Set the dropped file as the value of the input
    inputImage.files = files;
     
    dropArea.classList.remove('error')
     
    const event = new Event('change');
    inputImage.dispatchEvent(event);
   } else {
       // Display error message
       if (file.type !== 'image/webp') {
           errorMessage.textContent = "File you selected wasn't a webp image.";
        } else {
            errorMessage.textContent = 'File size exceeds 8MB.';
        }
        dropArea.classList.add('error')
    }
}
