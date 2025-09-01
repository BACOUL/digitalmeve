name: 💡 Feature Request
description: Suggest an idea, new feature, or improvement for DigitalMeve
labels: ["enhancement"]

body:
  - type: textarea
    id: problem
    attributes:
      label: ❓ Problem to Solve
      description: What problem would this feature solve?
    validations:
      required: true

  - type: textarea
    id: solution
    attributes:
      label: 🚀 Proposed Solution
      description: Describe the API/CLI/behavior you would like to see.

  - type: textarea
    id: alternatives
    attributes:
      label: 🔄 Alternatives
      description: Have you considered other solutions or workarounds?

  - type: textarea
    id: context
    attributes:
      label: 📎 Additional Context
      description: Any screenshots, references, or context that might help.
