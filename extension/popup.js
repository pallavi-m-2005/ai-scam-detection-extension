chrome.tabs.query(
  {
    active: true,
    currentWindow: true
  },

  async function(tabs) {

    const currentURL = tabs[0].url;

    document.getElementById("result").innerText =
      "Scanning: " + currentURL;

    try {

      const response = await fetch(
        "http://127.0.0.1:5000/scan",

        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            url: currentURL
          })
        }
      );

      const data = await response.json();

      document.getElementById("result").innerText =
        data.message;

    } catch (error) {

      document.getElementById("result").innerText =
        "⚠️ Backend offline";
    }
  }
);
