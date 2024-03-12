import React, { useState } from "react";

const TextArea = ({
  placeholder = "entrez du texte",
  style,
  basicStyle,
  defaultBorder = "none",
  color = "var(--light-color)",
  type = "text",
  value = "",
  setValue = null,
  name = "",
  emptyField = [],
  setEmptyField,
  ...content
}) => {
  const [defaultValue, setDefaultValue] = useState(value);

  const removeClassError = (name) => {
    if (setEmptyField) {
      setEmptyField(emptyField.filter((f) => f !== name));
    }
  };

  return (
    <textarea
      {...content}
      className={"inputTextDefault"}
      type={type}
      style={{
        resize: "none",
        overflow: "hidden",
        color,
        borderRadius: "10px",
        backgroundColor: "var(--primary)",
        padding: "10px",
        ...style,
        border: emptyField.includes(name)
          ? "solid 2px var(--error)"
          : defaultBorder,
        ...basicStyle,
      }}
      placeholder={placeholder}
      onChange={(e) =>
        setValue !== null
          ? setValue(e.target.value)
          : setDefaultValue(e.target.value)
      }
      value={setValue !== null ? value : defaultValue}
      onClick={() => removeClassError(name)}
    />
  );
};

export default TextArea;
