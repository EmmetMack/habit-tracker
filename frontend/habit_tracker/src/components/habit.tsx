

export default function Habit({name, description, frequency}: Props) {
    return (
        <div className = "border-solid border-2 border-color-black">
            <h1>Habit: {name}</h1>
            <h3>Description: {description}</h3>
            <h4>Frequency: {frequency}</h4>
        </div>
        
    );
}