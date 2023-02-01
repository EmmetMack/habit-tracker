

export default function Habit({name, description, frequency}: Props) {
    return (
        <div>
            <h1>Habit: {name}</h1>
            <h3>Description: {description}</h3>
            <h4>Frequency: {frequency}</h4>
        </div>
        
    );
}