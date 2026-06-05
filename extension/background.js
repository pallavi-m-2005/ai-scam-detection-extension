chrome.runtime.onInstalled.addListener(() => {

    console.log("AI Scam Detector Installed");
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {

    if (changeInfo.status === "complete") {

        console.log("Visited:", tab.url);
    }
});
