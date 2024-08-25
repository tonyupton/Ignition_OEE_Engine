SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OEE_Equipment](
	[EquipmentId] [uniqueidentifier] NOT NULL,
	[Name] [varchar](50) NULL,
	[Enterprise] [varchar](50) NULL,
	[Site] [varchar](50) NULL,
	[Area] [varchar](50) NULL,
	[WorkCenter] [varchar](50) NULL,
	[WorkUnit] [varchar](50) NULL,
	[UDTPath] [varchar](255) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[OEE_Equipment] ADD  CONSTRAINT [PK_OEE_Equipment] PRIMARY KEY CLUSTERED 
(
	[EquipmentId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
