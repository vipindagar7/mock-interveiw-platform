console.log("interview.js");


// open modal
const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})



// change domains in every second 

place = document.getElementById('dynamicDomains');

dynamicDomains = ['Front-end','Back-end','UX Design','Data Analytics','Full Stack']
let domain = 1

function changeDomain() {
    document.getElementById('dynamicDomains').textContent = dynamicDomains[domain];

    domain = (domain + 1) % dynamicDomains.length;
}

setInterval(() => {
    changeDomain()
}
, 1000);

