import Head from 'next/head';
import Image from 'next/image';
import { Inter } from '@next/font/google';
import styles from '@/styles/Home.module.css';
import Habit from '../components/habit';
import {getHabitsData} from '../libs/habits';
import HabitForm from '../components/habitForm';

const inter = Inter({ subsets: ['latin'] })

export async function getStaticProps() { 
  const allHabitsData = await getHabitsData();
  return {
    props: {
      allHabitsData,
    },
  }

}

export default function Home({allHabitsData}) {
  return (
    <>
      <Head>
        <title>Habit Tracker</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <h2>Habits:</h2>
        <ul>
          {allHabitsData.map(({id, name, description, frequency}) => (
            <li key={id}>
              <Habit name={name} description={description} frequency={frequency}/>
            </li>
          ))}
         
        </ul>
        <HabitForm />
      </main>
    </>
  )
}
