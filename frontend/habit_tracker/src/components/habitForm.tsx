import {useState} from 'react';
import {createHabit} from '../libs/habits';


export default function HabitForm() {
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [frequency, setFrequency] = useState("");


    async function handleSubmit(e) {
        if (!(name.length > 0) && !(description.length > 0)) {
            console.log("empty field values");
            return
            //add error element
        }
        let frequencyNum: int = 1
        if (frequency ==="weekly") {
            frequencyNum = 2;
        }
        else if (frequency === "monthly") {
            frequencyNum = 3;
        }
        
        const habitData : json = {
            name: name,
            description: description,
            frequency: frequencyNum
        };
        
        const habit = await createHabit(habitData);
        
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