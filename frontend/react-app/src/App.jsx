import './App.css'
import Header from './components/Header'
import Main from './components/Main'
import Footer from './components/Footer'

function App() {
  return (
    <div className='max-w-[800px] min-w-[400px] bg-white mx-auto'>
      <Header></Header>
      <Main></Main>
      <Footer></Footer>
    </div>
  )
}

export default App
