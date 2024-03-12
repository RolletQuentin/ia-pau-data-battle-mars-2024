import {
  ColorRect,
  HBox,
  Image,
  Link,
  MarginContainer,
  Text,
} from "@liro_u/react-components";
import React from "react";

const Footer = () => {
  // content customisation variable
  const leftText = "© 2010-2024 Kerdos Energy";
  const rightText = "KERDOS, les experts de votre transition écologique";
  const linkList = [
    {
      logoSrc: "/logo/linkedin.png",
      linkTo: "https://www.linkedin.com/company/kerdos-energy/",
    },
  ];

  // css customisation variable
  const logoSize = "25px";
  const logoContainerPercentage = 10;
  const verticalMargin = "10px";
  const horizontalMargin = "30px";
  const textFontSize = "large";
  const backgroundColor = "var(--dark-primary)";

  // css auto variable
  const textContainerPercentage = (100 - logoContainerPercentage) / 2;

  return (
    <ColorRect backgroundColor={backgroundColor}>
      <MarginContainer
        margin={verticalMargin}
        marginLeft={horizontalMargin}
        marginRight={horizontalMargin}
      >
        <HBox justifyContent="space-around">
          <Text
            text={leftText}
            fontSize={textFontSize}
            style={{ width: textContainerPercentage + "%" }}
          />
          <HBox
            style={{ width: logoContainerPercentage + "%" }}
            justifyContent="space-around"
          >
            {linkList.map((value, index) => {
              return (
                <Link href={value.linkTo} key={index} openNewWindow={true}>
                  <Image
                    src={value.logoSrc}
                    width={logoSize}
                    height={logoSize}
                  />
                </Link>
              );
            })}
          </HBox>
          <Text
            text={rightText}
            fontSize={textFontSize}
            style={{ width: textContainerPercentage + "%", textAlign: "end" }}
          />
        </HBox>
      </MarginContainer>
    </ColorRect>
  );
};

export default Footer;
