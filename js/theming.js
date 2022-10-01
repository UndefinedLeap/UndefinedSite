const stylesheet = document.documentElement.style;
const darkThemeMq = window.matchMedia("(prefers-color-scheme: dark)");

if(!localStorage.getItem("theme")){
    localStorage.setItem("theme", "system");
}

if(localStorage.getItem("theme") == "system") setSystemTheme();
else if(localStorage.getItem("theme") == "light") setLightTheme();
else if(localStorage.getItem("theme") == "dark") setDarkTheme();

setButtonText();

function setSystemTheme(){
    if(darkThemeMq.matches){
        setDarkTheme();
    }else{
        setLightTheme();
    }
    setButtonText();
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
    setButtonText();
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
    setButtonText();
}

function setButtonText(){
    const theme = localStorage.getItem("theme");
    var text = theme.toUpperCase() +' THEME';
    document.getElementById("btn").innerHTML = text;
}

darkThemeMq.addListener(e => {
    if(localStorage.getItem("theme") == "system"){
        if (e.matches) {
            setDarkTheme();
        } else {
            setLightTheme();
        }
    }
});

function setTheme(){
    if(localStorage.getItem("theme") == "system"){
        localStorage.setItem("theme", "light");
        setLightTheme();
    }else if(localStorage.getItem("theme") == "light"){
        localStorage.setItem("theme", "dark");
        setDarkTheme();
    }else{
        localStorage.setItem("theme", "system");
        setSystemTheme();
    }
}