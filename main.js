const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const axios = require('axios');

let win;

app.whenReady().then(() => {
    win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),  // ✅ Preload script added
            contextIsolation: true,  // ✅ Required for security
            enableRemoteModule: false,
            nodeIntegration: false  // ✅ Node.js functions ko disable kiya for security
        }
    });

    win.loadFile('index.html');
});

ipcMain.on('get-next-letter', async (event, userInput) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/generate_letter/", { user_input: userInput });
        event.reply('next-letter', response.data);
    } catch (error) {
        event.reply('next-letter', { error: "API error" });
    }
});
