import {useState} from 'react';


export default function HabitForm() {
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [frequency, setFrequency] = useState("");


    function handleSubmit(e) {
        alert(`Submitted lol ${name} ${description} ${frequency}`);
        //call function from libs that submits via the API
    }

    return(
        <form onSubmit={e => {handleSubmit(e)}}>
            <label>
                Name:
                <input type='text' value={name} onChange={e => {setName(e.target.value)}} />
            </label>
            <label>
                Description:
                <input type='text' value={description} onChange={e => {setDescription(e.target.value)}} />
            </label>
            <label>
                Frequency:
                <select value={frequency} onChange={e => {setFrequency(e.target.value)}}>
                    <option value="daily">Daily</option>
                    <option value="weekly">Weekly</option>
                    <option value="monthly">Monthly</option>
                </select>
            </label>
            <input type='submit' value="Submit"/>
        </form>
    )

}