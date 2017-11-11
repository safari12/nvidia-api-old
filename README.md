# nvidia-api
API for getting Nvidia GPU info

## Blueprints

### GPU

#### Models

- Name: `GPU`
    - REST
        - `methods`
            - GET
        - `prefix`
            - gpu
    - Properties
        - `name`
            - String
            - Required
        - `fan_speed`
            - Double
            - Required
        - `temperature`
            - Int
            - Required
        - `volatile`
            - Double
            - Required
            
- Name: `Watt`
    - Properties
        - `usage`
            - Int
            - Required
        - `cap`
            - Int
            - Required

- Name: `Memory`
    - Properties
        - `used`
            - Int
            - Required
        - `max`
            - Int
            - Required
            
#### Model Relations

- `GPU`
    - embeds one
        - `Watt`
            - Property name: `watt`
        - `Memory`
            - Property name: `memory`
