import './App.css'
import Header from './components/Header'
import Main from './components/Main'
import SearchBar from './components/SearchBar'

function App() {
  return (
    <div className='max-w-[800px] min-w-min bg-white mx-auto m-0'>
      <Header></Header>
      <SearchBar></SearchBar>
      <Main></Main>
    </div>
  )
}

export default App
