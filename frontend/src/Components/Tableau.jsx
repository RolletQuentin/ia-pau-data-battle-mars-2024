import { MarginContainer, Text } from "@liro_u/react-components";
import React from "react";

const Tableau = ({
  tab,
  color,
  titleFontWeight,
  titleFontSize,
  subSectionFontSize = "15",
  border = "solid 2px var(--dark-primary)",
  marginCase = "10px",
}) => {
  return (
    <table style={{ border, borderCollapse: "collapse" }}>
      {tab.map((line, index) => {
        return (
          <tr key={index} style={{ border, borderCollapse: "collapse" }}>
            {line.map((col, index) => {
              return (
                <td key={index} style={{ border, borderCollapse: "collapse" }}>
                  <MarginContainer margin={marginCase}>
                    <Text
                      text={col}
                      fontSize={subSectionFontSize + "px"}
                      color={color}
                    />
                  </MarginContainer>
                </td>
              );
            })}
          </tr>
        );
      })}
    </table>
  );
};

export default Tableau;
