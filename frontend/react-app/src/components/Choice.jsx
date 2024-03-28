// import { toast } from "react-toastify"
function Choice(props) {
  const { name, isChecked, setChoiceState, onPreferenceChange } = props
  const handleChange = () => {
    setChoiceState(!isChecked) // Toggle checkbox state
  }
  return (
    <div>
      <input
        id={name}
        checked={isChecked}
        type="checkbox"
        className="default:ring-2 mr-2"
        onChange={handleChange}
      />
      <label htmlFor="ml">{name}</label>
    </div>
  )
}

export default Choice
