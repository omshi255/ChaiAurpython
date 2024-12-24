```mermaid
graph TD
    username["username = 'hitesh'"]
    x --> y
    username -->|"chai aur code"| memory
    memory["chai aur code"]

    subgraph Memory
        15 --> x
        10 --> y
    end
