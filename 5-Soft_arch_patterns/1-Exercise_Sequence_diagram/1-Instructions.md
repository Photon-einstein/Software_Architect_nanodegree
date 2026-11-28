# Visualizing a User Interaction (Sequence Diagram)

## Context

In this exercise you will need to represent the interactions between a user and a centralized security and HVAC system.

### Your Task

A registered user, who is already logged in, uses the web dashboard to turn on a
mag-lock on an exterior door.

Create a Sequence Diagram that illustrates the synchronous request-response flow
for the scenario described above.

### Your diagram must include the following components:

- User's Browser: The starting point of the interaction.
- API Gateway: The single point of ingress for all client requests.
- Central Server: Responsible for a number of actions, including:
  - Checking if the user is logged in
  - Checking if the user is authorized to perform the action.
  - Issuing commands to devices
- Maglock device: Responsible for actioning commands issued by the central server
  and for reporting status back.

The diagram should clearly show the sequence of calls between these components,
starting from the user's click and ending with the final response.

## Instructions

You can create this diagram using any tool you prefer, such as draw.io (or another
graphical editor), Mermaid, or D2.

Create an image file (e.g., PNG, SVG) or a text file containing the diagram definition.
This exercise focuses on the clarity and accuracy of your diagram, not your choice of tool.

## Support information

[Mermaid guide](https://mermaid.js.org/syntax/sequenceDiagram.html)

Current status:

"Inline Alias Syntax
Alternatively, you can define an alias directly inside the configuration object using the "alias" field. This works with both participant and actor keywords:"
