Preserve the existing autonomous escalation policy. Select group by required user action and level independently by urgency. Use these Bark_notifications.notify parameters:

| Occasion | icon | group | level | sound |
|---|---|---|---|---|
| Routine information | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-info.png | Information | active | telegraph |
| Important finding | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-info.png | Information | timeSensitive | newsflash |
| Successful completion | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-success.png | Information | timeSensitive | fanfare |
| Work ready for review | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-review.png | Review | timeSensitive | fanfare |
| Decision required | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-question.png | Action Needed | timeSensitive | bell |
| Job blocked | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-blocked.png | Action Needed | timeSensitive | alarm |
| Task failed | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-failure.png | Action Needed if intervention required; otherwise Information | context-dependent | alarm |
| Critical intervention | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-urgent.png | Action Needed | critical | horn |
| Scheduled reminder | https://raw.githubusercontent.com/Hmmmmmmmmmm/case-assets/main/logos/case-reminder.png | Reminders | context-dependent | chime |

For critical alerts, set volume=10. Resolve context-dependent levels using the existing escalation policy. Do not add device keys to this configuration.
