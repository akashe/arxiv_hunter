function Choice(props) {
  const { name, isChecked, setChoiceState } = props;
  return (
    <div>
      <input
        id={name}
        checked={isChecked}
        type="checkbox"
        className="default:ring-2 mr-2"
        onChange={() => setChoiceState(!isChecked)}
      />
      <label htmlFor="ml">{name}</label>
    </div>
  );
}

export default Choice;
