import flet as ft
import re

def scan_message(msg):
    score = 0
    reasons = []
    msg_lower = msg.lower()

    if "urgent" in msg_lower or "now" in msg_lower or "immediately" in msg_lower:
        score += 30
        reasons.append("Urgency words detected")
    if re.search(r'http[s]?://', msg):
        score += 40
        reasons.append("Suspicious link found")
    if "ecocash" in msg_lower or "bank" in msg_lower or "win" in msg_lower or "lottery" in msg_lower:
        score += 20
        reasons.append("Impersonating service or too-good-to-be-true")

    if score >= 70:
        risk = "🔴 HIGH RISK - DO NOT CLICK"
    elif score >= 40:
        risk = "🟡 MEDIUM RISK - BE CAREFUL"
    else:
        risk = "🟢 LOW RISK - Looks safe"
    return risk, score, reasons

def main(page: ft.Page):
    page.title = "dzivisa-scam v10"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    input_box = ft.TextField(label="Paste suspicious SMS/WhatsApp message", multiline=True, min_lines=4)
    result_text = ft.Text(size=16, weight=ft.FontWeight.BOLD)

    def scan_click(e):
        if input_box.value.strip() == "":
            result_text.value = "⚠️ Paste a message first"
        else:
            risk, score, reasons = scan_message(input_box.value)
            reasons_text = "\n".join([f"• {r}" for r in reasons]) if reasons else "• No red flags found"
            result_text.value = f"{risk}\nScore: {score}/100\n{reasons_text}"
        page.update()

    page.add(
        ft.Text("🛡️ dzivisa-scam v10", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN),
        ft.Text("The Offline Guardian for Zimbabwe"),
        input_box,
        ft.ElevatedButton("SCAN MESSAGE", on_click=scan_click),
        result_text
    )

ft.run(main)
