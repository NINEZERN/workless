const clock = document.getElementById("clock");
const date = document.getElementById("clock-date");
const hourHand = document.querySelector(".clock-hand--hour");
const minuteHand = document.querySelector(".clock-hand--minute");
const elapsed = document.getElementById("elapsed");
const timeZone = clock.closest(".screen").dataset.timeZone;
const timeFormat = new Intl.DateTimeFormat("ru-RU", {
  timeZone, hour: "2-digit", minute: "2-digit", hourCycle: "h23",
});
const dateFormat = new Intl.DateTimeFormat("ru-RU", { timeZone, dateStyle: "medium" });
const startedAt = elapsed ? Number(elapsed.dataset.started) * 1000 : null;

function tick() {
  const now = new Date();
  const localTime = timeFormat.format(now);
  const [hours, minutes] = localTime.split(":").map(Number);
  clock.textContent = localTime;
  hourHand.style.setProperty("--rotation", `${(hours % 12) * 30 + minutes / 2}deg`);
  minuteHand.style.setProperty("--rotation", `${minutes * 6}deg`);
  date.textContent = dateFormat.format(now);

  if (elapsed) {
    const seconds = Math.max(0, Math.floor((now.getTime() - startedAt) / 1000));
    elapsed.textContent = [
      Math.floor(seconds / 3600),
      Math.floor((seconds % 3600) / 60),
      seconds % 60,
    ].map((part) => String(part).padStart(2, "0")).join(":");
  }
}

tick();
setInterval(tick, 1000);
