const stylesheet = document.documentElement.style;
const darkThemeMq = window.matchMedia("(prefers-color-scheme: dark)");

if(!localStorage.getItem("theme")){
    localStorage.setItem("theme", "system");
}

if(localStorage.getItem("theme") == "system") setSystemTheme();
setButtonText();

function setSystemTheme(){
    // if(localStorage.getItem("theme") == "system"){
        if(darkThemeMq.matches){
            setButtonText();
            setDarkTheme();
        }else{
            setButtonText();
            setLightTheme();
        }
    // }
}

function setDarkTheme(){
    const darkBg = getComputedStyle(document.documentElement).getPropertyValue("--dark-bg");
    const darkAccent = getComputedStyle(document.documentElement).getPropertyValue("--dark-accent");
    const darkAccent2 = getComputedStyle(document.documentElement).getPropertyValue("--dark-accent-2");
    const darkAccent3 = getComputedStyle(document.documentElement).getPropertyValue("--dark-accent-3");
    stylesheet.setProperty("--theme-bg", darkBg);
    stylesheet.setProperty("--theme-accent", darkAccent);
    stylesheet.setProperty("--theme-accent-2", darkAccent2);
    stylesheet.setProperty("--theme-accent-3", darkAccent3);
}

function setLightTheme(){
    const lightBg = getComputedStyle(document.documentElement).getPropertyValue("--light-bg");
    const lightAccent = getComputedStyle(document.documentElement).getPropertyValue("--light-accent");
    const lightAccent2 = getComputedStyle(document.documentElement).getPropertyValue("--light-accent-2");
    const lightAccent3 = getComputedStyle(document.documentElement).getPropertyValue("--light-accent-3");
    stylesheet.setProperty("--theme-bg", lightBg);
    stylesheet.setProperty("--theme-accent", lightAccent);
    stylesheet.setProperty("--theme-accent-2", lightAccent2);
    stylesheet.setProperty("--theme-accent-3", lightAccent3);
}

function setButtonText(){
    const theme = localStorage.getItem("theme");
    var text = theme.toUpperCase() +' THEME';
    document.getElementById("btn").innerHTML = text;
}

// darkThemeMq.addListener(e => {
//     if (e.matches) {
//         if(localStorage.getItem("theme") == "system"){
//             setButtonText();
//             setDarkTheme();
//         }
//     } else {
//         if(localStorage.getItem("theme") == "system"){
//             setButtonText();
//             setLightTheme();
//         }
//     }
// });

function setTheme(){
    if(localStorage.getItem("theme") == "system"){
        localStorage.setItem("theme", "light");
        setLightTheme();
        setButtonText();
    }else if(localStorage.getItem("theme") == "light"){
        localStorage.setItem("theme", "dark");
        setDarkTheme();
        setButtonText();
    }else{
        localStorage.setItem("theme", "system");
        setSystemTheme();
        setButtonText();
    }
}