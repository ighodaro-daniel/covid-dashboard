import axios from 'axios'
import { useState,useEffect,React} from 'react';
import Container from 'react-bootstrap/Container'
import 'bootstrap/dist/css/bootstrap.min.css'
import './style.css'
import Select from 'react-select'
import Card from './summaryCard';

function App() {
const [data , setData] = useState([])
const[summaryData,setSummaryData]=useState({})
const[activeLocation,setActiveLocation]=useState("NG")

const baseUrl = 'http://127.0.0.1:8000/info'
  const fetchData = async () => {
    try{
      
      const response = await axios.get(`${baseUrl}`);
      console.log(response.data)
      
      setData(response.data);
    }
      
    catch(error){
      console.error('error fetching data',error)

    }
  }

  const fetchSummaryData = async () => {
    try {
      const response = await axios.get(`${baseUrl}/${activeLocation}/`);
      setSummaryData(response.data);
      console.log(response.data)
    } catch (error) {
      console.error('Error fetching summary data:', error);
    }
  };
 
 useEffect(()=>{

fetchSummaryData()
},[activeLocation])

useEffect(()=>{
  fetchData();
},[])




 const locationList = [
  { value: "NG", label: "Nigeria" },
  { value: "GH", label: "Ghana" },
  { value: "MB", label: "Mozambique" },
  { value: "SA", label: "South Africa" },
  { value: "NI", label: "Niger" },
  { value: "TG", label: "Togo" },
  { value: "ZA", label: "Zambia" },
  { value: "BN", label: "Benin Republic" },
  { value: "CM", label: "Cameroun" },
  { value: "BT", label: "Botswana" },
  { value: "MA", label: "Mali" },
  { value: "ZI", label: "Zimbabwe" },
  { value: "AN", label: "Angola" },
];

  return (
    <div className='App' > 
      <Container fluid>
<h1>COVID-19 Dashboard</h1>
<div className="dashbord-container">
    <div className="dashboard-menu">
      <Select options={locationList}
      onChange={(selectedOption)=>
      setActiveLocation(selectedOption.value)}
      defaultValue = {locationList.filter(
        (options) => options.value === activeLocation
      )}

      className='dashboard-select'/>
      <p className='update-date'>Last updated :{summaryData.date_update}</p>
    </div>
    <div className="dashboard-summary">
<Card title='Total cases' value={summaryData.cases}/>

<Card title='Total Tests' value = {summaryData.test_completed}/>

<Card title = 'Total Deaths' value = {summaryData.deaths} />

<Card title = 'Total Vaccinated' value = {summaryData.vaccine_total_doses} />
 
 

    </div>
</div>


    
      </Container>
    </div>
  );
}

export default App;
