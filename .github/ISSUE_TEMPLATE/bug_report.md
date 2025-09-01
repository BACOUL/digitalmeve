name: 🐞 Bug Report
description: Report a problem, failed verification, or unexpected behavior in DigitalMeve
labels: ["bug"]

body:
  - type: textarea
    id: desc
    attributes:
      label: 📖 Description
      description: What happened? What did you expect instead?
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: 🪜 Steps to Reproduce
      description: Explain how to reproduce the issue.
      placeholder: |
        1. Run `digitalmeve generate ...`
        2. Verify file X
        3. Error appears
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: 🔖 DigitalMeve Version
      placeholder: "ex: 1.7.0"
    validations:
      required: true

  - type: dropdown
    id: python
    attributes:
      label: 🐍 Python Version
      options:
        - "3.10"
        - "3.11"
        - "3.12"
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: 📝 Logs / Screenshots
      description: Copy relevant logs, stack traces, or screenshots.
