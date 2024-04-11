// script.js
function assignColor(processName) {
    // This function generates and returns a color based on the process name
    const colors = ["blue", "yellow", "green", "red", "purple", "orange"];
    const index = processName.charCodeAt(0) % colors.length;
    return colors[index];
}
