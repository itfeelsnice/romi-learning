
let inp1 = document.querySelector("#inp1");
let btn1 = document.querySelector("#btn1");


let get1 = localStorage.getItem("save1");
let get2 = JSON.parse(get1);



btn1.addEventListener("click", () =>{
    let create1 = document.createElement("h1");
    input1 = inp1.value;
    localStorage.setItem("save1", JSON.stringify(input1));
    create1.textContent = input1;
    document.body.append(create1);
});















