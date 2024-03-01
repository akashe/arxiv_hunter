function Choice(props) {
  return (
    <div>
      <input
        id={props.name}
        type="checkbox"
        className="default:ring-2 mr-2"
      />
      <label htmlFor="ml">{props.name}</label>
    </div>
  );
}

export default Choice;
